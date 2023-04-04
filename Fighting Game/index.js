// Based on Chris Courses' tutorial: https://www.youtube.com/watch?v=3EMxBkqC4z0 with modifications

// Get the canvas element and the 2D context
const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d');

// Set the canvas dimensions and fill it with a black background
canvas.width = 1024;
canvas.height = 576;
c.fillRect(0, 0, canvas.width, canvas.height);

// Set the gravity constant
const gravity = 0.7;

// Define a Sprite class
class Sprite {
    constructor({ position, velocity, color = 'red', offset }) {
        // Initialize the sprite's position, velocity, height, and last key pressed
        this.position = position;
        this.velocity = velocity;
        this.width = 50;
        this.height = 150;
        this.lastKey = null;
        this.attackBox = {
            position: {
                x: this.position.x,
                y: this.position.y
            },
            offset,
            width: 100,
            height: 50
        };

        this.color = color;
        this.isAttacking = false;
        this.health = 420
    }

    // Draw the sprite
    draw() {
        c.fillStyle = this.color;
        c.fillRect(this.position.x, this.position.y, 50, 150);

        // draw attack box
        if (this.isAttacking) {
            c.fillStyle = 'blue';
            c.fillRect(this.attackBox.position.x, this.attackBox.position.y, this.attackBox.width, this.attackBox.height);
        }
    }

    // Update the sprite's position and velocity
    update() {
        this.draw()
        this.attackBox.position.x = this.position.x + this.attackBox.offset.x;
        this.attackBox.position.y = this.position.y

        this.position.x += this.velocity.x;
        this.position.y += this.velocity.y;

        // Apply gravity to the sprite if it is not on the ground
        if (this.position.y + this.height + this.velocity.y >= canvas.height) {
            this.velocity.y = 0;
        } else this.velocity.y += gravity;
    }

    attack() {
        this.isAttacking = true;
        setTimeout(() => {
            this.isAttacking = false;
        }, 100);
    }
}

// Create player and enemy sprites
const player = new Sprite({ position: { x: 0, y: 0 }, velocity: { x: 0, y: 0 }, offset: { x: 0, y: 0 } });
const enemy = new Sprite({ position: { x: 400, y: 100 }, velocity: { x: 0, y: 0 }, color: 'green', offset: { x: -50, y: 0 } });

// Define an object to keep track of which keys are pressed
const keys = {
        a: {
            pressed: false,
        },
        d: {
            pressed: false,
        },
        w: {
            pressed: false,
        },
        ArrowUp: {
            pressed: false,
        },
        ArrowRight: {
            pressed: false,
        },
        ArrowLeft: {
            pressed: false,
        },
    }
    // collision function
function RectCollision({ rectangle1, rectangle2 }) {
    return ((rectangle1.attackBox.position.x + rectangle1.attackBox.width >= rectangle2.position.x &&
        rectangle1.attackBox.position.x <= rectangle2.position.x + rectangle2.width &&
        rectangle1.attackBox.position.y + rectangle1.attackBox.height >= rectangle2.position.y &&
        rectangle1.attackBox.position.y <= rectangle2.position.y + rectangle2.height &&
        rectangle1.isAttacking))
}

//adjust timer
let timerId
let timer = 60

// Variable to track if the game is over
let gameOver = false;

function determineWinner(player, enemy, timerId) {
    clearTimeout(timerId)
    document.querySelector('#displayText').style.display = 'flex';
    if (player.health === enemy.health) {
        document.querySelector('#displayText').innerHTML = 'Tie!';

    } else if (player.health > enemy.health) {
        document.querySelector('#displayText').innerHTML = 'Player 1 Wins!';
    } else {
        document.querySelector('#displayText').innerHTML = 'Player 2 Wins!';
    }
    gameOver = true;
}

function deacreaseTimer() {
    if (timer > 0) {
        timerId = setTimeout(deacreaseTimer, 1000)
        timer--
        document.querySelector('#timer').innerHTML = timer
    }

    if (timer === 0) {
        determineWinner(player, enemy, timerId)
    }

}
deacreaseTimer()

// Define the animation loop
function animate() {
    window.requestAnimationFrame(animate);

    // Clear the canvas with a black background
    c.fillStyle = 'black'
    c.fillRect(0, 0, canvas.width, canvas.height)

    // Update the player and enemy sprites
    player.update();
    enemy.update();

    // Reset the horizontal velocities
    if (!keys.a.pressed && !keys.d.pressed) {
        player.velocity.x = 0;
    }


    if (!keys.ArrowRight.pressed && !keys.ArrowLeft.pressed) {
        enemy.velocity.x = 0;
    }

    // Apply horizontal velocity based on which keys are pressed
    if (keys.a.pressed && player.lastKey === 'a') {
        player.velocity.x = -5;
    } else if (keys.d.pressed && player.lastKey === 'd') {
        player.velocity.x = 5;
    } else if (keys.w.pressed && player.lastKey === 'w') {
        player.velocity.y = -15;
    }

    if (keys.ArrowRight.pressed) {
        enemy.velocity.x = 5;
    } else if (keys.ArrowLeft.pressed) {
        enemy.velocity.x = -5;
    } else if (keys.ArrowUp.pressed) {
        enemy.velocity.y = -15;
    }

    // detect collision
    if (!gameOver && RectCollision({ rectangle1: player, rectangle2: enemy }) && player.isAttacking) {
        player.isAttacking = false;
        const enemyHealthBar = document.querySelector('#enemyHealth');
        enemy.health -= 20; // You can change this value as needed
        enemyHealthBar.style.width = enemy.health + 'px';
        console.log('player collision');
    }

    if (!gameOver && RectCollision({ rectangle1: enemy, rectangle2: player }) && enemy.isAttacking) {
        enemy.isAttacking = false;
        const playerHealthBar = document.querySelector('#playerHealth');
        player.health -= 20; // You can change this value as needed
        playerHealthBar.style.width = player.health + 'px';
        playerHealthBar.style.marginLeft = (420 - player.health) + 'px'; // Update the margin-left to shift the health bar
        console.log('enemy collision');
    }

    //end game based on health
    if (!gameOver && (player.health <= 0 || enemy.health <= 0)) {
        gameOver = true;
        determineWinner(player, enemy, timerId);
    }

}

// Start the animation loop
animate();

// Listen for keydown events
window.addEventListener('keydown', (event) => {
    switch (event.key) {
        // Update the pressed state of the keys and the last key pressed
        case 'd':
            keys.d.pressed = true;
            player.lastKey = 'd';
            break;
        case 'a':
            keys.a.pressed = true;
            player.lastKey = 'a';
            break;
        case 'w':
            keys.w.pressed = true;
            player.lastKey = 'w';
            break;
        case ' ':
            player.attack();
            break;

        case 'ArrowUp':
            keys.ArrowUp.pressed = true;
            enemy.lastKey = 'ArrowUp';
            break;
        case 'ArrowRight':
            keys.ArrowRight.pressed = true;
            enemy.lastKey = 'ArrowRight';
            break;
        case 'ArrowLeft':
            keys.ArrowLeft.pressed = true;
            enemy.lastKey = 'ArrowLeft';
            break;
        case 'ArrowDown':
            enemy.attack();
            break;
    }
});

// Listen for keyup events
window.addEventListener('keyup', (event) => {
    switch (event.key) {
        // Update the pressed state of the keys
        case 'd':
            keys.d.pressed = false;
            break;
        case 'a':
            keys.a.pressed = false;
            break;
        case 'w':
            keys.w.pressed = false;
            break;

        case 'ArrowUp':
            keys.ArrowUp.pressed = false;
            break;
        case 'ArrowRight':
            keys.ArrowRight.pressed = false;
            break;
        case 'ArrowLeft':
            keys.ArrowLeft.pressed = false;
            break;
    }
});
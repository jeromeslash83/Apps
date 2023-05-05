document.addEventListener("DOMContentLoaded", function () {
    const addVisitForm = document.getElementById("addVisitForm");
    const visitList = document.getElementById("visitList");

    function loadVisits() {
        chrome.storage.sync.get("visits", function (data) {
            visitList.innerHTML = "";
            data.visits = data.visits || [];

            data.visits.forEach(function (visit, index) {
                const visitDiv = document.createElement("div");
                visitDiv.innerHTML = `
        <p>Site: ${visit.site}</p>
        <p>Date: ${visit.date}</p>
        <p>Status: ${visit.status}</p>
        <p>Tasks:</p>
        <ul>${Array.isArray(visit.tasks) ? visit.tasks.map(task => `<li><label><input type="checkbox"${task.checked ? ' checked' : ''}>${task.label}</label></li>`).join("") : ''}</ul>
        <button data-index="${index}">Delete</button>
    `;
                visitList.appendChild(visitDiv);
                const checkboxes = visitDiv.querySelectorAll("input[type='checkbox']");
                checkboxes.forEach(function (checkbox, checkboxIndex) {
                    checkbox.addEventListener("change", function () {
                        visit.tasks[checkboxIndex].checked = checkbox.checked;
                        chrome.storage.sync.set({ visits: data.visits });
                    });
                });
            });

            visitList.querySelectorAll("button").forEach(function (button) {
                button.addEventListener("click", function () {
                    const index = parseInt(this.dataset.index, 10);
                    data.visits.splice(index, 1);
                    chrome.storage.sync.set({ visits: data.visits }, loadVisits);
                });
            });
        });
    }

    addVisitForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const site = document.getElementById("site").value;
        const date = document.getElementById("date").value;
        const status = document.getElementById("status").value;
        const tasksText = document.getElementById("tasks").value;
        const tasks = tasksText
            .split("\n")
            .filter(task => task.trim() !== "")
            .map(task => ({ label: task.trim(), checked: false }));

        const newVisit = { site, date, status, tasks };

        chrome.storage.sync.get("visits", function (data) {
            data.visits = data.visits || [];
            data.visits.push(newVisit);
            chrome.storage.sync.set({ visits: data.visits }, function () {
                loadVisits();
                addVisitForm.reset();
            });
        });
    });

    loadVisits();
});

const taskInput = document.getElementById("task-input");
const addTaskBtn = document.getElementById("add-task-btn");
const tasksContainer = document.getElementById("tasks");
const message = document.getElementById("message");

const apiUrl = "/tasks";

async function fetchTasks() {
  const response = await fetch(apiUrl);
  if (!response.ok) {
    message.textContent = "Unable to load tasks.";
    return [];
  }
  return await response.json();
}

function renderTasks(tasks) {
  tasksContainer.innerHTML = "";
  if (tasks.length === 0) {
    tasksContainer.innerHTML = '<div class="no-tasks">No tasks yet. Add one above.</div>';
    return;
  }

  tasks.forEach((task) => {
    const card = document.createElement("div");
    card.className = `task-card ${task.done ? "done" : ""}`;

    const left = document.createElement("div");
    left.className = "task-left";

    const label = document.createElement("span");
    label.className = "task-label";
    label.textContent = task.task;

    const status = document.createElement("span");
    status.className = "task-status";
    status.textContent = task.done ? "Completed" : "Pending";

    left.append(label, status);

    const actions = document.createElement("div");
    actions.className = "task-actions";

    if (!task.done) {
      const doneButton = document.createElement("button");
      doneButton.className = "done-btn";
      doneButton.textContent = "Mark done";
      doneButton.addEventListener("click", async () => {
        await updateTaskDone(task.id);
      });
      actions.appendChild(doneButton);
    }

    const deleteButton = document.createElement("button");
    deleteButton.className = "delete-btn";
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", async () => {
      await deleteTask(task.id);
    });
    actions.appendChild(deleteButton);

    card.append(left, actions);
    tasksContainer.appendChild(card);
  });
}

async function loadTasks() {
  message.textContent = "";
  const tasks = await fetchTasks();
  renderTasks(tasks);
}

async function addNewTask() {
  const taskText = taskInput.value.trim();
  if (!taskText) {
    message.textContent = "Please enter a task.";
    return;
  }

  const response = await fetch(apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ task: taskText }),
  });

  if (!response.ok) {
    message.textContent = "Could not create task.";
    return;
  }

  taskInput.value = "";
  loadTasks();
}

async function updateTaskDone(taskId) {
  const response = await fetch(`${apiUrl}/${taskId}/done`, { method: "PUT" });
  if (!response.ok) {
    message.textContent = "Could not update task.";
    return;
  }
  loadTasks();
}

async function deleteTask(taskId) {
  const response = await fetch(`${apiUrl}/${taskId}`, { method: "DELETE" });
  if (!response.ok) {
    message.textContent = "Could not delete task.";
    return;
  }
  loadTasks();
}

addTaskBtn.addEventListener("click", addNewTask);
taskInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    addNewTask();
  }
});

loadTasks();

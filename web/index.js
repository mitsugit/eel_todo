async function getDataFromPython() {
    document.getElementById('myele').innerText = await eel.get_data()();
}

async function getTasks() {
    const tasks = await eel.get_tasks()()
    const divTasks = document.getElementById('tasks')
    divTasks.innerHTML = ''

    let taskDisplay = ''

    for (let task of tasks) {
        taskDisplay += `<p>${task}</p>`
    }

    divTasks.innerHTML = taskDisplay
}

document.getElementById('mybtn').addEventListener('click', async()=> {
    await eel.add(document.getElementById('taskinp').value)
    getTasks()
})

document.getElementById('sendbtn').addEventListener('click', async()=> {
    await eel.delete(document.getElementById('taskinp').value)
    getTasks()
})
async function getDataFromPython() {
    document.getElementById('myele').innerText = await eel.get_data()();
}

async function getTasks() {
    const tasks = await eel.get_tasks()()
    const divTasks = document.getElementById('tasks')
    divTasks.innerHTML = ''

    let taskDisplay = ''

    for (let task of tasks) {
        taskDisplay += `<p><input name="test" value=${task}></p>`
    }

    divTasks.innerHTML = taskDisplay
}

async function getBetlist() {
    const tasks = await eel.get_bet_list()()
    const divTasks = document.getElementById('betlist')
    divTasks.innerHTML = ''

    let taskDisplay = ''

    for (let task of tasks) {
        taskDisplay += `<p><input name="test" value=${task}></p>`
    }

    divTasks.innerHTML = taskDisplay
}



document.getElementById('mybtn').addEventListener('click', async()=> {
    await eel.add(document.getElementById('taskinp').value)
    getTasks()
})

document.getElementById('resetbtn').addEventListener('click', async()=> {
    await eel.reset()
    getTasks()
})

document.getElementById('getbtn').addEventListener('click', async()=> {
    var budget = document.getElementById('budget').value
    var gousei_odds = await eel.float_henkan(budget)()
    console.log(gousei_odds)
    document.getElementById('gousei_odds').value = gousei_odds
    getBetlist()

})
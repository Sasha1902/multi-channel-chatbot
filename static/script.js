async function getWeather() {
    let city = document.getElementById("city").value;
    let res = await fetch("/weather", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city: city })
    });
    let data = await res.json();
    document.getElementById("result").innerText = data.response;
}

async function bookAppointment() {
    let date = document.getElementById("date").value;
    let time = document.getElementById("time").value;
    let res = await fetch("/appointment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ date: date, time: time })
    });
    let data = await res.json();
    document.getElementById("result").innerText = data.response;
}
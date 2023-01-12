const eventBox = document.getElementById('event-box')
const countdownBox = document.getElementById('countdown-box')
const eventDate = Date.parse(eventBox.textContent)
console.log(eventDate);
const bidForm = document.getElementById('bid-form')
const winnerText = document.getElementById('winner-text')
setInterval(() => {

  const now = new Date().getTime()

  const diff = eventDate - now
  console.log(diff)

  const d = Math.floor(eventDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
  const h = Math.floor((eventDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
  const m = Math.floor((eventDate / (1000 * 60) - (now / (1000 * 60))) % 60)
  const s = Math.floor((eventDate / (1000) - (now / (1000))) % 60)
  if (diff > 0) {
    countdownBox.innerHTML = `<h4>${d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds"}</h4>`
    winnerText.innerHTML = ""

  } else {
    countdownBox.innerHTML = `<h4>Auction Expired.</h4>`
    bidForm.innerHTML = ""

  }
}, 1000)

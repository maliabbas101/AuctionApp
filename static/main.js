const eventBox = document.getElementById('event-box')
const countdownBox = document.getElementById('countdown-box')
const eventDate = Date.parse(eventBox.textContent)

setInterval(() => {

  const now = new Date().getTime()

  const diff = eventDate - now

  const d = Math.floor(eventDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
  const h = Math.floor((eventDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
  const m = Math.floor((eventDate / (1000 * 60) - (now / (1000 * 60))) % 60)
  const s = Math.floor((eventDate / (1000) - (now / (1000))) % 60)
  if (diff > 0) {
    countdownBox.innerHTML = `<h4>${d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds"}</h4>`

  } else {
    countdownBox.innerHTML = `<h4>Auction Expired.</h4>`
  }
}, 1000)

// const bidAmount = document.getElementById('bid-amount')
// console.log(bidAmount.value)
$("#bid-amount").change(function () {
  var startPrice = document.getElementById("bid-amount").value;

});

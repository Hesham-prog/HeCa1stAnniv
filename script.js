const anniversaryDate = new Date("2026-04-03T00:00:00+07:00");
const countdownElement = document.getElementById("countdown");
const heartsContainer = document.querySelector(".floating-hearts");

function updateCountdown() {
  const now = new Date();
  const diff = anniversaryDate.getTime() - now.getTime();

  if (diff <= 0) {
    countdownElement.textContent = "Hari ini hari anniversary kita.";
    return;
  }

  const totalSeconds = Math.floor(diff / 1000);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  countdownElement.textContent = `${hours} jam ${minutes} menit ${seconds} detik`;
}

function spawnHeart() {
  const heart = document.createElement("span");
  heart.className = "heart";
  heart.textContent = "\u2665";
  heart.style.left = `${Math.random() * 100}%`;
  heart.style.animationDuration = `${7 + Math.random() * 5}s`;
  heart.style.fontSize = `${14 + Math.random() * 18}px`;
  heartsContainer.appendChild(heart);

  window.setTimeout(() => {
    heart.remove();
  }, 12000);
}

updateCountdown();
window.setInterval(updateCountdown, 1000);
window.setInterval(spawnHeart, 900);

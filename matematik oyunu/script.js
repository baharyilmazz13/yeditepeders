let level = 0;
let currentAnswer;


const questionEl = document.getElementById("soru");
const answerInput = document.getElementById("cevapKutusu");
const btnAnswer = document.getElementById("btn");

const btnWater = document.getElementById("btnSu");
const btnSun = document.getElementById("btnGunes");

const plant = document.getElementById("cicek");
const levelText = document.getElementById("levelAlani");
const message = document.getElementById("message");


function generateQuestion() {
    const a = Math.floor(Math.random() * 10) + 1;
    const b = Math.floor(Math.random() * 10) + 1;
    const op = Math.random() > 0.5 ? "+" : "-";

    currentAnswer = op === "+" ? a + b : a - b;

    questionEl.textContent = `${a} ${op} ${b} = ?`;
    answerInput.value = "";
}


function updatePlant() {
    plant.className = "cicek level" + level;

    if (level === 10) {
        plant.textContent = "🌸";
        plant.classList.add("flower");
        message.textContent = "Tebrikler! Bitkin çiçek açtı! 🌸🎉";
        btnWater.classList.add("hide");
        btnSun.classList.add("hide");
    }

    levelText.textContent = `Seviye: ${level} / 10`;
}


btnAnswer.addEventListener("click", () => {
    const userAnswer = Number(answerInput.value);

    if (userAnswer === currentAnswer) {
        message.textContent = "Doğru! Şimdi su veya güneş verebilirsin.";
        btnWater.classList.remove("hide");
        btnSun.classList.remove("hide");

        if (level < 10) {
            level++;
            updatePlant();
        }
    } else {
        message.textContent = "Yanlış! Tekrar dene.";
    }

    generateQuestion();
});


function extraGrow() {
    if (level < 10) {
        level++;
        updatePlant();
    }

    btnWater.classList.add("hide");
    btnSun.classList.add("hide");
}

btnWater.addEventListener("click", extraGrow);
btnSun.addEventListener("click", extraGrow);
function rainFlowers() {
    for (let i = 0; i < 40; i++) {
        const flower = document.createElement("div");
        flower.classList.add("flower-rain");
        flower.textContent = "🌸";


        flower.style.left = Math.random() * 100 + "vw";
        flower.style.animationDelay = Math.random() * 3 + "s";
        flower.style.fontSize = (20 + Math.random() * 30) + "px";

        document.body.appendChild(flower);


        setTimeout(() => flower.remove(), 4000);
    }
}

generateQuestion();
updatePlant();

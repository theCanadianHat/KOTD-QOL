document.addEventListener("DOMContentLoaded", () => {
    fetch("/")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("boss-list");
            data.forEach(boss => {
                const item = document.createElement("li");
                item.innerHTML = `<a href="${boss.url}" target="_blank">${boss.title}</a>`;
                item.innerHTML += `<span>${boss.flair}</span>`
                list.appendChild(item);
            });
        });
});
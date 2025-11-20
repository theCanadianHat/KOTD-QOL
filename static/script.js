const get_boss_stats = (button) => {
    url = button.getAttribute('data-url');

    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log('Boss scouted:', data);
            // Optionally update the DOM
        })
        .catch(error => console.error('Error:', error));

}
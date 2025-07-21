fetch('https://replit.com/@thanishqranbir/farlix-backend')
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById("videoList");
    data.forEach(video => {
      list.innerHTML += `
        <div>
          <h2>${video.title}</h2>
          <iframe src="${video.url}" allowfullscreen></iframe>
          <p>${video.description}</p>
        </div>
      `;
    });
  });

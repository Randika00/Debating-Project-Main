url = `https://nmps--2021.herokuapp.com/api/v1/tournaments/nmps2021/speakers`
fetch(url)
    .then(response => response.json())
    .then(speakers => { console.log(speakers); })



    try {
        // ⛔️ TypeError: Failed to fetch
        // 👇️ incorrect or incomplete URL
        const response = await fetch('https://nmps--2021.herokuapp.com/api/v1/tournaments/nmps2021/speakers');
    
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
    
        const result = await response.json();
        console.log(result)
      } catch (err) {
        console.log(err);
      }
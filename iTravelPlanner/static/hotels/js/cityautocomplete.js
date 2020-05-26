const search = document.getElementById('searchcity');
const matchList = document.getElementById('match-list');

// Search State Code
const searchCities = async searchText => {
    //const res = await fetch('{% static url '../data/city_codes.json' %}');
    const res = await fetch('../data/city_codes.json');
    const states = await res.json();

    // Get matches to current text input
    let matches = states.filter(state => {
        const regex = new RegExp(`^${searchText}`,`gi`);
        return state.IATA.match(regex) || state.City.match(regex);
    });

    if(searchText.matches === 0) {
        matches = []
    }

    outputHtml(matches);

    console.log(matches);
};

// show results
const outputHtml = matches => {
    if matches.length > 0 {
        const html = matches.map(match => `
            <div class="card card-body">
                <h4>${match.IATA} </h4>
            </div>
        `).join('');
        console.log(html);
    }
}

search.addEventListener('input', () => searchCities(search.value));



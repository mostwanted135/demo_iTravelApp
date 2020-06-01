const search = document.getElementById('searchcity');
const matchList = document.getElementById('match-list');

// Search State Code
const searchCities = async searchText => {
    //const res = await fetch('https://cdn.rawgit.com/VarunAravinth/CC_TravelPlanner_TeamWydah/Hotel_app/iTravelPlanner/static/hotels/data/city_codes.json?token=APOA66WWXEDOPK2JHWVNUUS6Z3XWK');
    const res = await fetch('https://raw.githubusercontent.com/mostwanted135/iTravelApp_Json_file/master/city_codes.json');
    const states = await res.json();
    // Get matches to current text input
    let matches = states.filter(state => {
        const regex = new RegExp(`^${searchText}`,'gi');
        return state.IATA.match(regex) || state.City.match(regex);
    });
    if (searchText.length === 0) {
        matches = [];
    }
    outputHtml(matches);
};

// show results
const outputHtml = matches => {
    if ( matches.length > 0 ) {
        const html = matches.map(match => `
            <div class="card card-body mb-1">
                <h4> ${match.IATA} </h4>
            </div>
        `
        ).join('');
        console.log(html);
        matchList.innerHTML = html;
    }
};

search.addEventListener('input', () => searchCities(search.value))
;



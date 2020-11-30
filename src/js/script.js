 
let filepath = "heroes_dict.json" 
let boxDiv = document.getElementById("boxDiv")
let tooltipDiv = document.getElementById("tooltipDiv")
let labelsDiv = document.getElementById("labelsDiv")
let searchbar = document.getElementById("searchbar")

// fetch JSON file with infos
function getHeroInfo(hero_name) {
    fetch(filepath)
    .then(response => { 
        return response.json();
    })
    .then(data => {
        parseInformation(hero_name, data[hero_name])
    })
}

function parseInformation (hero_name, hero_data) {
    hero_data.forEach(element => {
        let tokens = element.split("$")
        let ability_name = tokens[0]
        let ability_description = tokens[1]
        createBox(ability_name, ability_description)
    });
}

function createBox(ability_name, ability_description) {
    let label = document.createElement("label")
    let tooltip = document.createElement("p")
    console.log(boxDiv)
    boxDiv.className= "boxDiv"
    label.className = "abilityLabel"
    label.innerHTML = ability_name
    tooltip.className = "popup"
    tooltip.innerText = ability_description
    label.onmouseover = () => {
        tooltip.style.display = 'inline'
    }
    label.onmouseleave = () => {
        tooltip.style.display = 'none'
    }
    tooltipDiv.appendChild(tooltip)
    labelsDiv.appendChild(label)
}

function getRequestedHero(event) {
    searchbar = document.getElementById("searchbar")
    let input = searchbar.value.toLowerCase()
    // if (event.keyCode == 13) {
        // let tooltipDiv = document.getElementById("tooltipDiv")
        // let labelsDiv = document.getElementById("labelsDiv")
        tooltipDiv.innerHTML=""
        labelsDiv.innerHTML=""
        getHeroInfo(input)
    // }
}

function clearButton() {
    searchbar.value = "";
    tooltipDiv.innerHTML=""
    labelsDiv.innerHTML=""
}
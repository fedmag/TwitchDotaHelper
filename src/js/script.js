 
let filepath = "WebScraper.json" 
let boxDiv = document.getElementById("boxDiv")
let tooltipDiv = document.getElementById("tooltipDiv")
let labelsDiv = document.getElementById("labelsDiv")
let searchbar = document.getElementById("searchbar")
let clearBtn = document.getElementById("clearBtn")
searchbar.addEventListener('keyup', getRequestedHero)
clearBtn.addEventListener('click', clearButton)

function getRequestedHero() {
    let input = searchbar.value.trim().toLowerCase()
    console.log(input)
    tooltipDiv.innerHTML=""
    labelsDiv.innerHTML=""
    getHeroInfo(input)
}

// fetch JSON file with infos
function getHeroInfo(hero_name) {
    fetch(filepath)
    .then(response => { 
        return response.json();
    })
    .then(data => {
        parseInformation(data[hero_name])
    })
}

function parseInformation (heroData) {
    heroData.forEach(element => {
        if (element != "") {
            splitted = element.split("\n") 
            name = splitted[0]
            descr = splitted.slice(2, -2)
            descr = descr.join("\n")
            createBox(name, descr)
        }
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

function clearButton() {
    searchbar.value = "";
    tooltipDiv.innerHTML=""
    labelsDiv.innerHTML=""
}
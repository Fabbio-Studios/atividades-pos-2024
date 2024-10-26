let currentPokemon = 1;

export async function fetchPokemonData(pokemonId) {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}`);
        const pokemonData = await response.json();

        // Cálculo da média de status
        const stats = pokemonData.stats;
        const totalStats = stats.reduce((sum, stat) => sum + stat.base_stat, 0);
        const averageStats = (totalStats / stats.length).toFixed(2); // Média com duas casas decimais

        return { pokemonData, averageStats };
    } catch (error) {
        console.error('Erro ao buscar dados do Pokémon:', error);
    }
}

export function updatePokemonInfo(pokemonId) {
    fetchPokemonData(pokemonId).then(({ pokemonData, averageStats }) => {
        const pokemonInfo = document.getElementById('pokemon-info');
        pokemonInfo.classList.remove('show');
        pokemonInfo.classList.add('fade');

        setTimeout(() => {
            document.getElementById('name').innerText = `Nome: ${capitalize(pokemonData.name)}`;
            document.getElementById('national-dex').innerText = `Número: ${pokemonData.id}`;

            // Usando sprites GIF do Showdown
            const frontGif = pokemonData.sprites.other.showdown.front_default;
            const backGif = pokemonData.sprites.other.showdown.back_default;
            document.getElementById('sprite').src = frontGif || pokemonData.sprites.front_default;
            document.getElementById('sprite-back').src = backGif || pokemonData.sprites.back_default;

            document.getElementById('average-status').innerText = `Média de Status: ${averageStats}`;

            // Limpa os spans de tipos anteriores
            const typeContainer = document.getElementById('type');
            typeContainer.innerHTML = '';

            // Adiciona cada tipo com um span colorido
            pokemonData.types.forEach(type => {
                const typeSpan = document.createElement('span');
                typeSpan.classList.add('type', `type-${type.type.name}`);
                typeSpan.innerText = capitalize(type.type.name);
                typeContainer.appendChild(typeSpan);
            });

            // Guardando o link do choro
            const cryUrl = `https://play.pokemonshowdown.com/audio/cries/${pokemonData.name}.mp3`;
            document.getElementById('cry').dataset.cryUrl = cryUrl;

            pokemonInfo.classList.remove('fade');
            pokemonInfo.classList.add('show');
        }, 500);
    });
}

export function playCry() {
    const cryUrl = document.getElementById('cry').dataset.cryUrl;
    const audio = new Audio(cryUrl);
    audio.play();
}

export function previousPokemon() {
    if (currentPokemon > 1) {
        currentPokemon--;
        updatePokemonInfo(currentPokemon);
    }
}

export function nextPokemon() {
    if (currentPokemon < 1025) {
        currentPokemon++;
        updatePokemonInfo(currentPokemon);
    }
}

export function goToPokemon() {
    const searchNumber = document.getElementById('searchNumber').value;
    if (searchNumber >= 1 && searchNumber <= 1025) {
        currentPokemon = searchNumber;
        updatePokemonInfo(currentPokemon);
    } else {
        alert("Digite um número entre 1 e 1025.");
    }
}

export async function searchPokemon() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${searchInput}`);
        if (!response.ok) throw new Error('Pokémon não encontrado'); // Verifica se a resposta é válida
        const pokemonData = await response.json();
        
        if (pokemonData.id >= 1 && pokemonData.id <= 1025) {
            currentPokemon = pokemonData.id;
            updatePokemonInfo(currentPokemon);
        } else {
            alert('Este Pokémon não existe.');
        }
    } catch (error) {
        alert('Pokémon não encontrado.'); // Exibe um alerta em caso de erro
        console.error('Erro na busca do Pokémon:', error); // Log do erro para o console
    }
}


// Capitaliza a primeira letra do nome
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

import './style.css'
import { updatePokemonInfo, previousPokemon, nextPokemon, goToPokemon, searchPokemon, playCry } from './api.js';

window.onload = () => {
    updatePokemonInfo(1); // Carrega o primeiro Pokémon ao iniciar a página

    document.getElementById('searchInput').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            searchPokemon(); // Chama a função de pesquisa
        }
    });

    document.getElementById('prev-button').addEventListener('click', previousPokemon);
    document.getElementById('next-button').addEventListener('click', nextPokemon);
    document.getElementById('go-button').addEventListener('click', goToPokemon);
    document.querySelector('.btn-cry').addEventListener('click', playCry); // Adiciona o evento de clique
}

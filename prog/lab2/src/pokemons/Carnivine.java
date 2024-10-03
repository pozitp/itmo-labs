package pokemons;

import moves.physical.Crunch;
import moves.physical.Facade;
import moves.status.StunSpore;
import moves.status.Swagger;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Carnivine extends Pokemon {
    public Carnivine(String name, int level) {
        super(name, level);
        setType(Type.GRASS);
        setStats(74, 100, 72, 90, 72, 46);
        setMove(new Crunch(), new StunSpore(), new Swagger(), new Facade());
    }
}

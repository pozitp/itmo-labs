package pokemons;

import moves.status.Confide;
import moves.status.ScaryFace;
import moves.status.Swagger;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Zorua extends Pokemon {
    public Zorua(String name, int level) {
        super(name, level);
        setType(Type.DARK);
        setStats(40, 65, 40, 80, 40, 65);
        setMove(new ScaryFace(), new Swagger(), new Confide());
    }
}

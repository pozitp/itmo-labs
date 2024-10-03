package pokemons;

import moves.special.Flamethrower;
import moves.status.Confide;
import moves.status.ScaryFace;
import moves.status.Swagger;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Zoroark extends Pokemon {
    public Zoroark(String name, int level) {
        super(name, level);
        setType(Type.DARK);
        setStats(60, 105, 60, 120, 60, 105);
        setMove(new ScaryFace(), new Swagger(), new Confide(), new Flamethrower());
    }
}

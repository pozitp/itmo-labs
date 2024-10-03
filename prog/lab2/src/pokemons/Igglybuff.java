package pokemons;

import moves.status.DefenseCurl;
import moves.status.ThunderWave;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Igglybuff extends Pokemon {
    public Igglybuff(String name, int level) {
        super(name, level);
        setType(Type.NORMAL, Type.FAIRY);
        setStats(90, 30, 15, 40, 20, 15);
        setMove(new DefenseCurl(), new ThunderWave());
    }
}

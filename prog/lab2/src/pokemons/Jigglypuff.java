package pokemons;

import moves.special.HyperVoice;
import moves.status.DefenseCurl;
import moves.status.ThunderWave;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Jigglypuff extends Pokemon {
    public Jigglypuff(String name, int level) {
        super(name, level);
        setType(Type.NORMAL, Type.FAIRY);
        setStats(115, 45, 20, 45, 25, 20);
        setMove(new DefenseCurl(), new ThunderWave(), new HyperVoice());
    }
}

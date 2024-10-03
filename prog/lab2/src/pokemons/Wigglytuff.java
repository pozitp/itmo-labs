package pokemons;

import moves.special.HyperVoice;
import moves.status.DefenseCurl;
import moves.status.DoubleTeam;
import moves.status.ThunderWave;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Wigglytuff extends Pokemon {
    public Wigglytuff(String name, int level) {
        super(name, level);
        setType(Type.NORMAL, Type.FAIRY);
        setStats(140, 70, 45, 85, 50, 45);
        setMove(new DefenseCurl(), new ThunderWave(), new HyperVoice(), new DoubleTeam());
    }
}

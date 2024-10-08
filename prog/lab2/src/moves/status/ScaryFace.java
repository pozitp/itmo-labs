package moves.status;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class ScaryFace extends StatusMove {
    public ScaryFace() {
        super(Type.NORMAL, 0, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        pokemon.setMod(Stat.SPEED, -2);
    }

    @Override
    protected String describe() {
        return "is using Scary Face. The user frightens the target with a scary face to harshly lower its Speed stat";
    }
}

package moves.physical;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Status;
import ru.ifmo.se.pokemon.Type;

public class Facade extends PhysicalMove {
    public Facade() {
        super(Type.NORMAL, 70, 100);
    }

    @Override
    protected void applyOppDamage(Pokemon pokemon, double damage) {
        switch (pokemon.getCondition()) {
            case BURN, POISON, PARALYZE -> super.applyOppDamage(pokemon, damage * 2);
            default -> super.applyOppDamage(pokemon, damage);
        }
    }

    @Override
    protected String describe() {
        return "is using Facade. The user crunches up the target with sharp fangs. This may also lower the target’s Defense stat";
    }
}

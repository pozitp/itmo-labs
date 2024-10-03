package moves.special;

import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class HyperVoice extends SpecialMove {
    public HyperVoice() {
        super(Type.NORMAL, 90, 100);
    }

    //    TODO I can't do soundproof check bruh

    @Override
    protected String describe() {
        return "is using Hyper Voice. The user attacks by letting loose a horribly loud, resounding cry";
    }

    //    FIXME Do I need to write attack to multiple foes? How can I do this?
}

import pokemons.*;
import ru.ifmo.se.pokemon.Battle;

public class Main {
    public static void main(String[] args) {
        // initialize the battle
        Battle b = new Battle();

        // initialize pokemons
        Carnivine carnivine = new Carnivine("Carnivine", 1);
        Zorua zorua = new Zorua("Zorua", 1);
        Zoroark zoroark = new Zoroark("Zoroark", 1);
        Igglybuff iglybuff = new Igglybuff("Iglybuff", 1);
        Jigglypuff jigglypuff = new Jigglypuff("Jigglypuff", 1);
        Wigglytuff wigglytuff = new Wigglytuff("Wigglytuff", 1);

        // first team
        b.addAlly(carnivine);
        b.addAlly(zorua);
        b.addAlly(zoroark);

        // second team
        b.addFoe(iglybuff);
        b.addFoe(jigglypuff);
        b.addFoe(wigglytuff);

        // start the battle
        b.go();
    }
}
import model.Knopochka;
import model.Neznaika;
import model.WandStory;
import model.objects.ShoeType;
import model.objects.Shoes;

public class Starter {
    public static void start() {
        Neznaika neznaika = new Neznaika();
        Knopochka knopochka = new Knopochka();
        Shoes shoes = new Shoes(ShoeType.RED);

        WandStory story = new WandStory(neznaika, knopochka, shoes);
        story.tell();
    }
}

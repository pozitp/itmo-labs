package model;

import model.abstracted.Person;

public class Neznaika extends Person {
    private boolean isWishingForWand;

    public Neznaika() {
        super("Незнайка");
        isWishingForWand = true;
    }

    public boolean isWishingForWand() {
        return isWishingForWand;
    }

    public void setWishingForWand(boolean wishing) {
        this.isWishingForWand = wishing;
    }

    public void lookAt(Object object) {
        System.out.println(name + " разглядывает " + object.toString());
    }

    public void wave() {
        System.out.println(name + " махнул рукой");
    }

    @Override
    public void speak(String message) {
        System.out.println(name + " рассказывает \"" + message + "\"");
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }

    @Override
    public String toString() {
        return name;
    }
}

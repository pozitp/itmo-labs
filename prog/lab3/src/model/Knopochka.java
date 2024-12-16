package model;

import model.abstracted.Person;

public class Knopochka extends Person {
    public Knopochka() {
        super("Кнопочка");
    }

    @Override
    public void speak(String message) {
        System.out.println(name + " говорит \"" + message + "\"");
    }

    public void giveAdvide() {
        speak("нужно совершать хорошие поступки бескорыстно");
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Knopochka that = (Knopochka) o;
        return name.equals(that.name);
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

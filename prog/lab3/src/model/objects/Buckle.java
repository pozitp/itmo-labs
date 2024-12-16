package model.objects;

public record Buckle(String shape) {
    @Override
    public String toString() {
        return "пряжкой в виде " + shape;
    }
}
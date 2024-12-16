package model.objects;

public enum ShoeType {
    RED("красные"), BLUE("синие"), GREEN("зеленые");

    private final String text;

    ShoeType(String text) {
        this.text = text;
    }

    @Override
    public String toString() {
        return text;
    }
}
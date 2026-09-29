package model;

public class Book {
    private String privateTitle = "private";
    String packageTitle = "package";
    protected String protectedTitle = "protected";
    public String publicTitle = "public";

    private String title;
    private String author;
    private int year;
    public static int count;
    public final int id;

    public Book() {
        this("Без назви", "Невідомий автор", 0);
    }

    public Book(String title) {
        this(title, "Невідомий автор", 0);
    }

    public Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
        this.id = ++count;
    }

    public String info() {
        return id + ": " + title + " — " + author + ", " + year;
    }
}

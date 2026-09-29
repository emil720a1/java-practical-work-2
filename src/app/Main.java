package app;

import model.Book;

public final class Main {
    private Main() {
    }

    public static void main(String[] args) {
        Book first = new Book();
        Book second = new Book("Кобзар");
        Book third = new Book("Java", "Herbert Schildt", 2022);

        System.out.println(first.info());
        System.out.println(second.info());
        System.out.println(third.info());
        System.out.println(Book.count);
    }
}

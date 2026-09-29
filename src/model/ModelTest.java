package model;

public final class ModelTest {
    private ModelTest() {
    }

    public static void check(Book book) {
        System.out.println(book.packageTitle);
        System.out.println(book.protectedTitle);
        System.out.println(book.publicTitle);
    }
}

class Foo {
    private Semaphore f;
    private Semaphore s;

    public Foo() {
        f=new Semaphore(0);
        s=new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        f.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        f.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        s.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        s.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}

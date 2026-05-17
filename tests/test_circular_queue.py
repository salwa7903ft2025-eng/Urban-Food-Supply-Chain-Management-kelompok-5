from circular_queue import CircularQueue


def main():
    queue = CircularQueue(5)

    print("Tambah data")
    queue.enqueue("Produk A")
    queue.enqueue("Produk B")
    queue.enqueue("Produk C")

    queue.tampilkan_buffer()

    print("\nHapus data")
    print(queue.dequeue())

    print("\nIsi queue sekarang")
    queue.tampilkan_buffer()

    print("\nPeek:")
    print(queue.peek())

    print("\nPenuh?")
    print(queue.is_full())

    print("\nPanjang queue:")
    print(len(queue))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item_degrades_in_quality(self):
        items = [Item("Elixir of the Mongoose", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_quality_never_negative(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
            items = [Item("Aged Brie", 2, 0)]
            GildedRose(items).update_quality()
            self.assertEqual(1, items[0].quality)
            self.assertEqual(1, items[0].sell_in)

    def test_backstage_passes_increase_quality_by_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(21, items[0].quality)


    
if __name__ == '__main__':
    unittest.main()

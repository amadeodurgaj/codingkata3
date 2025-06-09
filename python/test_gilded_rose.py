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

    def test_backstage_passes_increase_quality_by_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increase_quality_by_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 2, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)   

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].quality)

    def test_quality_bounds(self):
        items = [
            Item("Aged Brie", 1, 50),
            Item("Elixir of the Mongoose", 1, 0),
            Item("Conjured Mana Cake", 0, 1),
        ]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(0, items[1].quality)
        self.assertEqual(0, items[2].quality)

    
    
if __name__ == '__main__':
    unittest.main()

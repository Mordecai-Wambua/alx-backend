import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
const app = express();
const port = 1245;
const getAsync = promisify(client.get).bind(client);

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  try {
    const val = await getAsync(`item.${itemId}`);
    return val;
  } catch (err) {
    console.error(err);
  }
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const stock = await getCurrentReservedStockById(itemId);
  const available_stock =
    stock !== null ? stock : item.initialAvailableQuantity;
  item.currentQuantity = available_stock;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const stock = await getCurrentReservedStockById(itemId);
  const available_stock =
    stock !== null ? stock : item.initialAvailableQuantity;

  if (available_stock < 1) {
    return res.json({
      status: 'Not enough stock available',
      itemId,
    });
  }

  const newStock = available_stock - 1;
  reserveStockById(itemId, newStock);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

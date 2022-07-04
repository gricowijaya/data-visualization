const getTitle = (array) => { 
  const categoryName = [];
  const title = [];
  const price = [];
  const womanFashion = [];
  for (let index = 0; index < array.length; index++) {
    categoryName.push(array[index].categoryName)
    title.push(array[index].title);
    price.push(array[index].price);
  }

      categoryName: categoryName,
      title: title,
      price: price,
  return womanFashion;
}

msg.payload = getTitle(msg.payload);

return msg;

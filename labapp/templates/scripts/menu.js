jQuery(() => {
    $(".header_navigation [href]").each(function () { //выбираем все элементы внутри класса "header_navigation", у которых есть атрибут href, и для каждого из них выполняем функцию

        if (this.href == window.location.href) { //Проверка, равен ли адрес ссылки элемента (this.href) текущему адресу страницы (window.location.href). Если это условие выполняется, значит текущий элемент ссылается на текущую страницу.
            $(this).addClass("active");          //Добавляем класс "active"
        }
    });
});

function printTable() {

}

let click_1 = 0; let click_2 = 0;

function sortTableByColumn(table, column, order, count) {
    console.log(table.rows);
    if (count % 2 === 0) {
        const isAsc = order === 'asc';
        const rows = table.rows;
        for (let i = 1; i < rows.length; i++) {
            const td = rows[i].cells[column];
            const previousRow = rows[i - 1];
            const previousTd = previousRow.cells[column];

            let shouldSwitch = null;
            if (isAsc) {
                // Сортировка по возрастанию
                shouldSwitch = td.textContent.toLowerCase() < previousTd.textContent.toLowerCase();
            } 
        
            else {
            // Сортировка по убыванию
                shouldSwitch = td.textContent.toLowerCase() > previousTd.textContent.toLowerCase();
            }

            // Перемещение строк, если они должны быть переставлены
            if (shouldSwitch && i > 1) {
                rows[i].parentNode.insertBefore(rows[i], rows[i - 1]);
            }
        } 
    }
    else {
        const isAsc = order === 'asc';
        const rows = table.rows;
        for (let i = 1; i < rows.length; i++) {
            const td = rows[i].cells[column];
            const previousRow = rows[i - 1];
            const previousTd = previousRow.cells[column];

            let shouldSwitch = null;
            if (!isAsc) {
                // Сортировка по возрастанию
                shouldSwitch = td.textContent.toLowerCase() < previousTd.textContent.toLowerCase();
            } 
            else {
                // Сортировка по убыванию
                shouldSwitch = td.textContent.toLowerCase() > previousTd.textContent.toLowerCase();
            }

            // Перемещение строк, если они должны быть переставлены
            if (shouldSwitch && i > 1) {
                rows[i].parentNode.insertBefore(rows[i], rows[i - 1]);
            }
        } 
    }
}

// function sortTableByColumn(table, column, order) {
//     const isAsc = order === 'asc';
//     const rows = table.rows;
//     for (let i = 1; i < rows.length; i++) {
//         const td = rows[i].cells[column];
//         const previousRow = rows[i - 1];
//         const previousTd = previousRow.cells[column];

//         let shouldSwitch = null;
//         if (isAsc) {
//             // Сортировка по возрастанию
//             shouldSwitch = compareStrings(td.textContent, previousTd.textContent);
//         } else {
//             // Сортировка по убыванию
//             shouldSwitch = compareStrings(previousTd.textContent, td.textContent);
//         }

//         // Перемещение строк, если они должны быть переставлены
//         if (shouldSwitch) {
//             rows[i].parentNode.insertBefore(rows[i], rows[i - 1]);
//         }
//     }
// }

// function compareStrings(str1, str2) {
//     return str1.localeCompare(str2);
// }

// function sortTableByColumn(table, column, order) {
//     const isAsc = order === 'asc';
//     const rows = table.rows;
//     for (let i = 1; i < rows.length; i++) { // Начинаем с второй строки, чтобы пропустить заголовки
//         const td = rows[i].cells[column];
//         const previousRow = rows[i - 1];
//         const previousTd = previousRow.cells[column];

//         let shouldSwitch = null;
//         if (isAsc) {
//             // Сортировка по возрастанию
//             shouldSwitch = td.textContent.toLowerCase() < previousTd.textContent.toLowerCase();
//         } else {
//             // Сортировка по убыванию
//             shouldSwitch = td.textContent.toLowerCase() > previousTd.textContent.toLowerCase();
//         }

//         // Перемещение строк, если они должны быть переставлены
//         if (shouldSwitch) {
//             rows[i].parentNode.insertBefore(rows[i], rows[i - 1]);
//         }
//     }
// }

// function sortTable(tableSelector, columnIndex) {
//     // Получаем все строки таблицы
//     const rows = document.querySelectorAll(tableSelector + ' tbody tr');
  
//     // Массив для хранения значений ячеек каждой строки
//     const values = [];
  
//     // Проходим по всем строкам и заполняем массив значениями
//     rows.forEach(row => {
//       const cellValue = row.querySelectorAll('td')[columnIndex].textContent;
//       values.push(parseFloat(cellValue));
//     });
  
//     // Сортируем массив значений
//     let sortedValues = values.slice();
//     for (let i = 1; i < sortedValues.length; i++) {
//       for (let j = i + 1; j < sortedValues.length; j++) {
//         if (sortedValues[i] > sortedValues[j]) {
//           [sortedValues[i], sortedValues[j]] = [sortedValues[j], sortedValues[i]];
//         }
//       }
//     }
  
//     // Если количество вызовов четное, то сортируем по убыванию
//     if (columnIndex % 2 === 0) {
//       sortedValues.reverse();
//     }
  
//     // Устанавливаем отсортированные значения обратно в таблицу
//     rows.forEach((row, index) => {
//       row.querySelectorAll('td')[columnIndex].textContent = sortedValues[index];
//     });
//   }


function sortGrid(tbody, colNum, type, count) {
    
    
    let rowsArray = Array.from(tbody.rows);

    // compare(a, b) сравнивает две строки, нужен для сортировки

    let compare;
    if (count % 2 === 0) {
        switch (type) {
        case 'number':
            compare = function(rowA, rowB) {
            return rowA.cells[colNum].innerHTML - rowB.cells[colNum].innerHTML;
            };
            break;
        case 'string':
            compare = function(rowA, rowB) {
            return rowA.cells[colNum].innerHTML > rowB.cells[colNum].innerHTML ? 1 : -1;
            };
            break;
        }   
    }
    else {
        switch (type) {
            case 'number':
                compare = function(rowA, rowB) {
                return rowB.cells[colNum].innerHTML - rowA.cells[colNum].innerHTML;
                };
                break;
            case 'string':
                compare = function(rowA, rowB) {
                return rowB.cells[colNum].innerHTML > rowA.cells[colNum].innerHTML ? 1 : -1;
                };
                break;
            }   
    }
    // сортировка
    rowsArray.sort(compare);

    tbody.append(...rowsArray); 
  }
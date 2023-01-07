document.addEventListener("DOMContentLoaded", init);

function init() {
    const committeesListId = 'committees-list';
    const candidatesListId = 'candidates-list';

    const committeesListNode = document.querySelector(`#${committeesListId}`);
    const candidatesListNode = document.querySelector(`#${candidatesListId}`);
    const startPeriodNode = document.querySelector('#start-period');
    const endPeriodNode = document.querySelector('#end-period');
    const makeReportBtnNode = document.querySelector('button');  // возьмёт первый на странице, что и требуется
    const instructionsMsgNode = document.querySelector('#instrucion-msg');  // МОЖЕТ НЕ БЫТЬ - отчёта на его месте

    // юзаем вычисляемые св-ва (ES6+)
    const dictOfOppositeSelectorsNodes = {
        [committeesListId]: candidatesListNode,
        [candidatesListId]: committeesListNode
    }

    // только один select может быть с отмеченными позициями - у другого надо их снимать
    function clearSelectedOppositeOptions(currentSelectNode) {
        const oppositeSelectNode = dictOfOppositeSelectorsNodes[currentSelectNode.id];

        if (!oppositeSelectNode) {
            console.log('Нет противоположного select! id текущего: ', currentSelectNode.id);
            return false;
        }

        for (let o of oppositeSelectNode.options) {
            o.selected = false;
        }
    }

    // для проверки заполнения периода и сравнения, что начало < конца
    function getTimestamp(strTime, countFractions) {
        let fractions = strTime.split('-');

        if (fractions.length !== countFractions) {
            return null;
        }

        let [year, month, day] = fractions;
        let date = new Date(year, month, day);
        return date.getTime();
    }

    // для проверки наличия выбранной позиции
    function isHaveSelectedOption(select) {
        for (let o of select.options) {
            if (o.selected == true) {
                return true;
            }
        }
        return false;
    }

    // проверка заполнения всех необходимых полей для разблокировки возможности формирования отчёта
    function isFieldsReady() {
        let isCommitteesSelectReady = isHaveSelectedOption(committeesListNode);
        let isCandidatesSelectReady = isHaveSelectedOption(candidatesListNode);

        // иммитация XOR
        const onlyOneSelectReady = !(isCommitteesSelectReady === isCandidatesSelectReady);

        if (!onlyOneSelectReady) {
            return false;
        }

        // раз retrun'a не было, значит только один селект заполнен
        // если даты заполнены, то будет отмашка о готовности полей
        let startPeriod = getTimestamp(startPeriodNode.value, 3);
        let endPeriod = getTimestamp(endPeriodNode.value, 3);

        const isCorrectPeriods = (startPeriod !== null) && (endPeriod !== null);
        if (!isCorrectPeriods) {
            return false;
        }

        // раз дошли сюда - всё ок, делаем последнюю проверку, что начало < конца
        return startPeriod < endPeriod;
    }

    function changeDisabledStatusForMakeReportBtn() {
        cl = instructionsMsgNode && instructionsMsgNode.classList;

        if (!isFieldsReady()) {
            makeReportBtnNode.disabled = true;
            cl && cl.remove('hidden');
            return false;
        }

        makeReportBtnNode.disabled = false;
        cl && cl.add('hidden');
    }

    // каждое изменение поля select это сброс отмеченных позиций для противоположного select (из условий задания)
    function handleClickOnSelect(event) {
        const node = event.currentTarget || event.target;

        clearSelectedOppositeOptions(node);
        changeDisabledStatusForMakeReportBtn();
    }

    // назначаем обработчики
    committeesListNode.addEventListener('change', handleClickOnSelect);
    candidatesListNode.addEventListener('change', handleClickOnSelect);
    startPeriodNode.addEventListener('input', changeDisabledStatusForMakeReportBtn);
    endPeriodNode.addEventListener('input', changeDisabledStatusForMakeReportBtn);
}

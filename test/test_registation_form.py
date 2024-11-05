import os
from selene import (
    browser,
    command,
    have
)

def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element("#firstName").type("Vesta")
    browser.element("#lastName").type("Parfenova")
    browser.element("#userEmail").type("test051124@test.ru")
    browser.element('[name=gender][value=Female]+label').click()
    browser.element("#userNumber").type("1234567890")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select option[value="1984"]').click()
    browser.element('.react-datepicker__month-select option[value="9"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--022').click()
    browser.element('#subjectsInput').type('Maths').press_tab()
    browser.element('//label[contains(text(),"Sports")]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test.jpeg'))
    browser.element('#currentAddress').type('Mykop')
    browser.element("#react-select-3-input").type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            'Vesta Parfenova',
            'test051124@test.ru',
            'Female',
            '1234567890',
            '22 October,1984',
            'Maths',
            'Sports',
            'test.jpeg',
            'Mykop',
            'NCR Delhi',
        )
    )

    # browser.element('//table//td[contains(text(),"Student Name")]/../td[2]').should(have.text('Vesta Parfenova'))
    # browser.element('//table//td[contains(text(),"Student Email")]/../td[2]').should(have.text('test051124@test.ru'))
    # browser.element('//table//td[contains(text(),"Gender")]/../td[2]').should(have.text('Female'))
    # browser.element('//table//td[contains(text(),"Mobile")]/../td[2]').should(have.text('1234567890'))
    # browser.element('//table//td[contains(text(),"Date of Birth")]/../td[2]').should(have.text('22 October,1984'))
    # browser.element('//table//td[contains(text(),"Subjects")]/../td[2]').should(have.text('Maths'))
    # browser.element('//table//td[contains(text(),"Hobbies")]/../td[2]').should(have.text('Sports'))
    # browser.element('//table//td[contains(text(),"Picture")]/../td[2]').should(have.text('image.png'))
    # browser.element('//table//td[contains(text(),"Address")]/../td[2]').should(have.text('homeland'))
    # browser.element('//table//td[contains(text(),"State and City")]/../td[2]').should(have.text('Uttar Pradesh Merrut'))

def test_python_search(main_page):
    main_page.open()
    main_page.search("pycon")
    assert "No results found." not in main_page.page_source()
    main_page.quit()

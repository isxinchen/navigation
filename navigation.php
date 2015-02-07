<?php

class Category{
	var $c_id
	var $c_name;
    var $c_index;
    var $c_items;

    public function __construct(){
        $this->c_items = new Array();
    }

    public function addItem($name = NULL, $url = NULL; $index = -1){
        $this->c_items;
    }
}

class Item{
	var $i_id;
    var $i_name;
	var $i_url;
	var $i_index;
}

$categories = new Array();

function addCategory(){
    $category = new Category();
    $category->c_id = 0;
    $category->c_name = "test";
    $category->c_index = 1;
    categories->append(category);
}
?>

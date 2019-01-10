//
//  SecondViewController.swift
//  To Do List
//
//  Created by Tom Rooney on 10/28/18.
//  Copyright © 2018 Thomas J. Rooney. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var textField: UITextField!
    
    @IBAction func add(_ sender: Any) {
        
        let itemsObject = UserDefaults.standard.object(forKey: "items")
        
        var items:[String]
        
        if let tempItems = itemsObject as? [String]{
            
            items = tempItems
            
            items.append(textField.text!)
            
        } else {
            
            items = [textField.text!]
            
        }
        
        UserDefaults.standard.set(items, forKey: "items")
        
        textField.text = ""
    }
    
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        
        self.view.endEditing(true)
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        
        textField.resignFirstResponder()
        
        return true
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }


}


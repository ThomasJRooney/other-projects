//
//  ViewController.swift
//  Cat Years
//
//  Created by Tom Rooney on 10/25/18.
//  Copyright © 2018 Thomas J. Rooney. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var catOutput: UILabel!
    
    @IBAction func buttonClicked(_ sender: UIButton) {
        let ageInCatYears = Int(textField.text!)! * 7
        
        catOutput.text = String(ageInCatYears)
    }
    
    
 
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }


}


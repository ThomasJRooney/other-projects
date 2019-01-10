//
//  ViewController.swift
//  Is it Prime?
//
//  Created by Tom Rooney on 10/27/18.
//  Copyright © 2018 Thomas J. Rooney. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var theNumberEntered: UITextField!
    @IBOutlet weak var theOutcome: UILabel!
    
    @IBAction func buttonPressed(_ sender: Any) {
        if let userEnteredString = theNumberEntered.text {
            let integerTheNumberEntered = Int(userEnteredString)
            if let number = integerTheNumberEntered {
                var isPrime = true
                if number == 1 {
                    isPrime = false
                }
                var i = 2
                while i < number {
                    if number % i == 0{
                        isPrime = false
                    }
                    i += 1
                }
                if isPrime {
                    theOutcome.text = "\(number) is prime!"
                } else {
                    theOutcome.text = "\(number) is not prime!"
                }
            } else {
                theOutcome.text = "Please enter a positive whole number"
            }
        
        }
    
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

}



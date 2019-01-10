//
//  ViewController.swift
//  How Many Fingers?
//
//  Created by Tom Rooney on 10/26/18.
//  Copyright © 2018 Thomas J. Rooney. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var outCome: UILabel!
    @IBOutlet weak var theGuess: UITextField!
    
    @IBAction func guessButtonClicked(_ sender: UIButton) {
        let diceRoll = arc4random_uniform(6)
        if Int(theGuess.text!)! == diceRoll {
            outCome.text = "Correct! It was a \(diceRoll)"
        } else {
            outCome.text = "Incorrect! It was a \(diceRoll)"
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }


}


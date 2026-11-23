import { Component } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
@Component({
  imports: [FormsModule, RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected submitted = false;
  protected alertMessage = '';
  protected readonly maxDate = new Date(
    Date.now() - new Date().getTimezoneOffset() * 60_000,
  )
    .toISOString()
    .slice(0, 10);
  protected formData = this.emptyForm();
  protected register(form: NgForm): void {
    if (form.invalid) {
      form.control.markAllAsTouched();
      const emailControl = form.controls['email'];
      const phoneControl = form.controls['phone'];
      const messages: string[] = [];

      if (emailControl?.invalid) {
        messages.push(
          emailControl.hasError('required')
            ? 'Email is required.'
            : 'Enter a valid Gmail address ending in @gmail.com.',
        );
      }
      if (phoneControl?.invalid) {
        messages.push(
          phoneControl.hasError('required')
            ? 'Phone number is required.'
            : 'Enter a valid 10-digit Indian phone number.',
        );
      }

      this.alertMessage =
        messages.join(' ') || 'Please complete all required fields correctly.';
      return;
    }
    this.alertMessage = '';
    this.submitted = true;
  }

  protected clearAlert(): void {
    this.alertMessage = '';
  }

  protected registerAnother(): void {
    this.formData = this.emptyForm();
    this.submitted = false;
    this.alertMessage = '';
  }
  private emptyForm(): {
    name: string;
    email: string;
    age: string;
    course: string;
    dob: string;
    phone: string;
    address: string;
  } {
    return {
      name: '',
      email: '',
      age: '',
      course: '',
      dob: '',
      phone: '',
      address: '',
    };
  }
}